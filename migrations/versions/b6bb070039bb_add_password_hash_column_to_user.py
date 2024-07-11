"""Add password_hash column to User

Revision ID: b6bb070039bb
Revises: 7bb0e99a6248
Create Date: 2024-07-11 13:14:43.626463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6bb070039bb'
down_revision = '7bb0e99a6248'
branch_labels = None
depends_on = None


def upgrade():
    # Add the password_hash column with a default value
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=False, server_default='default_hash_value'))
    
    # Update existing records to set a default value for password_hash
    op.execute("UPDATE users SET password_hash = 'default_hash_value' WHERE password_hash IS NULL")

    # Add the NOT NULL constraint
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('password_hash', nullable=False)


def downgrade():
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('password_hash', nullable=True)
    
    op.drop_column('users', 'password_hash')