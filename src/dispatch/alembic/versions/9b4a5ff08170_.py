"""Add JSON column to Incident Type table to allow for plugin metadata

Revision ID: 9b4a5ff08170
Revises: a32bfbb4bcaa
Create Date: 2020-05-19 09:25:22.688248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9b4a5ff08170"
down_revision = "a32bfbb4bcaa"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "incident_type",
        sa.Column("plugin_metadata", sa.JSON(), server_default="{}", nullable=False),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("incident_type", "plugin_metadata")
    # ### end Alembic commands ###
