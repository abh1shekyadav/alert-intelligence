"""create enriched_alerts table

Revision ID: aa2348bc0119
Revises: c7d9895fca67
Create Date: 2025-11-09 10:47:25.556777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa2348bc0119'
down_revision: Union[str, Sequence[str], None] = 'c7d9895fca67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'enriched_alerts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('alert_id', sa.Integer, sa.ForeignKey('alerts.id', ondelete='CASCADE')),
        sa.Column('summary', sa.String, nullable=False),
        sa.Column('tags', sa.JSON, nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False)
    )

def downgrade() -> None:
    op.drop_table('enriched_alerts')