"""empty message

Revision ID: d9441ec1b050
Revises: 
Create Date: 2025-02-15 10:48:07.015382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9441ec1b050'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_number', sa.String(length=50), nullable=False),
    sa.Column('washroom_seat_type', sa.String(length=10), nullable=False),
    sa.Column('floor_number', sa.String(length=50), nullable=False),
    sa.Column('condition', sa.String(length=50), nullable=False),
    sa.Column('single_bed', sa.Integer(), nullable=False),
    sa.Column('double_bed', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('room_number')
    )
    op.create_table('visitor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('father_name', sa.String(length=100), nullable=False),
    sa.Column('cnic', sa.String(length=15), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cnic')
    )
    op.create_table('visit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('vehicle_number', sa.String(length=20), nullable=False),
    sa.Column('persons', sa.Integer(), nullable=False),
    sa.Column('rooms', sa.JSON(), nullable=False),
    sa.Column('checkin_date', sa.Date(), nullable=False),
    sa.Column('checkout_date', sa.Date(), nullable=False),
    sa.Column('visitor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['visitor_id'], ['visitor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('visit_information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vehicle_number', sa.String(length=50), nullable=True),
    sa.Column('checkin_date', sa.DateTime(), nullable=False),
    sa.Column('checkout_date', sa.DateTime(), nullable=True),
    sa.Column('men', sa.Integer(), nullable=False),
    sa.Column('women', sa.Integer(), nullable=False),
    sa.Column('children', sa.Integer(), nullable=False),
    sa.Column('total_people', sa.Integer(), nullable=False),
    sa.Column('visit_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['visit_id'], ['visit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visit_information')
    op.drop_table('visit')
    op.drop_table('visitor')
    op.drop_table('room')
    # ### end Alembic commands ###
