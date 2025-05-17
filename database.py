from sqlmodel import SQLModel, create_engine, Session

# Database URL (SQLite in this case)
DATABASE_URL = "sqlite:///circadia.db"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=False)

# Function to create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency to get DB session
def get_session():
    with Session(engine) as session:
        yield session
