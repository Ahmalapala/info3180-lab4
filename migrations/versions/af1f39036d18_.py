"""empty message

Revision ID: af1f39036d18
Revises: dd85ded686b8
Create Date: 2023-02-26 21:25:53.796697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af1f39036d18'
down_revision = 'dd85ded686b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###