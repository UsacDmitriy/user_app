from typing import Optional
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

from app.config import Config


class DatabaseClient:
    def __init__(self, config: Config, tables: Optional[list[str]]):
        self.config = config
        self.engine = create_engine(self.config.host, future=True)
        self.session = Session(bind=self.engine, future=True)
        self.metadata = MetaData(self.engine)
        self._metadata.reflect()
        if tables:
            self._set_internal_database_tables(tables)


    def _reflect_metadate(self) -> None:
        self.metadata.reflect()

    def _set_internal_database_tables(self, tables: list[str]):
        for table in tables:
            setattr(self, table, self.metadata.tables[table])