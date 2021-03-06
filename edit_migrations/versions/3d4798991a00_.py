"""empty message

Revision ID: 3d4798991a00
Revises: 34a3e495a6c4
Create Date: 2022-06-14 19:20:57.537315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d4798991a00'
down_revision = '34a3e495a6c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('UPDATE person SET completed = TRUE WHERE completed IS NULL;')
    op.alter_column('person', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('person', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
