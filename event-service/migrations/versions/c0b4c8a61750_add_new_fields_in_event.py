"""add new fields in event

Revision ID: c0b4c8a61750
Revises: 7835dd36e331
Create Date: 2024-11-26 16:02:24.880837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0b4c8a61750'
down_revision: Union[str, None] = '7835dd36e331'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'events',
        sa.Column('number_of_tickets', sa.Integer(), server_default="0", nullable=False)
    )
    op.add_column('events', sa.Column('organizer_id', sa.String(length=255), server_default='unknown', nullable=False))
    op.add_column('events',
                  sa.Column('organizer_name', sa.String(length=255), server_default='unknown', nullable=False))
    op.add_column('events', sa.Column('organizer_email', sa.String(length=255), server_default='unknown@example.com',
                                      nullable=False))

    # ### end Alembic commands ###

    with op.batch_alter_table('events') as batch_op:
        batch_op.alter_column('number_of_tickets', server_default=None)


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'organizer_email')
    op.drop_column('events', 'organizer_name')
    op.drop_column('events', 'organizer_id')
    op.drop_column('events', 'number_of_tickets')
    # ### end Alembic commands ###