"""empty message

Revision ID: bf20ca20c9ee
Revises: 95941a1969c2
Create Date: 2018-11-26 23:08:19.934188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf20ca20c9ee'
down_revision = '95941a1969c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('checkup_checkup_report_key', 'checkup', type_='unique')
    op.drop_constraint('checkup_checkup_type_key', 'checkup', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('checkup_checkup_type_key', 'checkup', ['checkup_type'])
    op.create_unique_constraint('checkup_checkup_report_key', 'checkup', ['checkup_report'])
    # ### end Alembic commands ###