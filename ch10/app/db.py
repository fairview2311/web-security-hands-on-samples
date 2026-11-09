"""演習用データ。起動とリセットで学習開始時の状態に戻す。"""
import hashlib
import hmac
import secrets
import sqlite3
from contextlib import contextmanager
from pathlib import Path

SCRYPT_N, SCRYPT_R, SCRYPT_P = 16384, 8, 1


def hash_password(password):
    salt = secrets.token_bytes(16)
    digest = hashlib.scrypt(password.encode(), salt=salt,
                            n=SCRYPT_N, r=SCRYPT_R, p=SCRYPT_P)
    return f"scrypt${salt.hex()}${digest.hex()}"


def verify_password(password, stored):
    try:
        _, salt_hex, digest_hex = stored.split("$")
    except ValueError:
        return False
    digest = hashlib.scrypt(password.encode(), salt=bytes.fromhex(salt_hex),
                            n=SCRYPT_N, r=SCRYPT_R, p=SCRYPT_P)
    return hmac.compare_digest(digest.hex(), digest_hex)

DB_PATH = Path("/data/midori.db")


@contextmanager
def connect():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except BaseException:
        conn.rollback()
        raise
    finally:
        conn.close()


def reset():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with connect() as conn:
        conn.executescript("""
            DROP TABLE IF EXISTS sessions;
            DROP TABLE IF EXISTS notes;
            DROP TABLE IF EXISTS coupons;
            DROP TABLE IF EXISTS secrets;
            DROP TABLE IF EXISTS users;
            CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT UNIQUE,
                display_name TEXT, password_hash TEXT, is_admin INTEGER DEFAULT 0,
                bio TEXT DEFAULT '', points INTEGER DEFAULT 0);
            CREATE TABLE notes(id INTEGER PRIMARY KEY, owner_id INTEGER,
                title TEXT, body TEXT, is_public INTEGER DEFAULT 0);
            CREATE TABLE sessions(sid TEXT PRIMARY KEY, user_id INTEGER);
            CREATE TABLE coupons(code TEXT PRIMARY KEY, points INTEGER, used INTEGER DEFAULT 0);
            CREATE TABLE secrets(name TEXT PRIMARY KEY, value TEXT);
        """)
        # わざと弱い MD5。パスワードはどれもよくある弱いもの（総当たりの単語リストに載る）
        def h(pw):
            return hash_password(pw)
        conn.executemany(
            "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, 0)",
            [(1, "yamada-taro", "山田 太郎", h("password1"), 0, "開発チームです"),
             (2, "sato-hanako", "佐藤 花子", h("iloveyou"), 0, "営業チームです"),
             (3, "admin", "管理者", h("sunshine"), 1, "管理担当です")],
        )
        conn.executemany("INSERT INTO notes VALUES (?, ?, ?, ?, ?)", [
            (1, 1, "山田のメモ", "来週の打ち合わせは月曜日です。", 1),
            (2, 2, "佐藤の個人メモ", "新商品のアイデア", 0),
            (3, 3, "管理者の秘密メモ", "FLAG{broken-access-control}", 0),
        ])
        conn.execute("INSERT INTO coupons VALUES ('MIDORI100', 100, 0)")
        conn.execute("INSERT INTO secrets VALUES ('database_flag', 'FLAG{sql-injection}')")
