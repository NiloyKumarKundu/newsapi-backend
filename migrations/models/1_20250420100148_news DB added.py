from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "news" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "title" TEXT,
    "desc" TEXT,
    "url" TEXT,
    "published_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" BIGINT REFERENCES "user" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "news";"""
