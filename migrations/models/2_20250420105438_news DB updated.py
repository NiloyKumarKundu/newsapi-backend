from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "news" DROP CONSTRAINT IF EXISTS "fk_news_user_f58031f9";
        ALTER TABLE "news" DROP COLUMN "user_id";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "news" ADD "user_id" BIGINT;
        ALTER TABLE "news" ADD CONSTRAINT "fk_news_user_f58031f9" FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE CASCADE;"""
