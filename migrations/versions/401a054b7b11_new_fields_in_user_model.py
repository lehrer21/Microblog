"""new fields in user model

Revision ID: 401a054b7b11
Revises: 473633d31691
Create Date: 2023-01-08 13:44:56.943251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '401a054b7b11'
down_revision = '473633d31691'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
