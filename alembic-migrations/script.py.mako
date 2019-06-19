"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

WARNING: DO NOT IMPORT YOUR MODELS FOR DATA MIGRATIONS

Best practice is to re-define the models you need inline here. If your model code
changes over time in non-backwards compatible ways, importing them here will
produce unpredictable results, especially with rollbacks.

"""

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

def upgrade():
    ${upgrades if upgrades else "pass"}


def downgrade():
    ${downgrades if downgrades else "pass"}
