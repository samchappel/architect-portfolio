"""create tables

Revision ID: 3615fb6a69b5
Revises: 
Create Date: 2023-06-09 15:52:44.256576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3615fb6a69b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portfolio_grids',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('highlight_image', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('preview', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('_password_hash', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('access_code', sa.Integer(), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('grid_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('images', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['grid_id'], ['portfolio_grids.id'], name=op.f('fk_project_details_grid_id_portfolio_grids')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project_details')
    op.drop_table('users')
    op.drop_table('portfolio_grids')
    # ### end Alembic commands ###
