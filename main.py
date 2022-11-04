from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from models.a import A
from models.b import B

engine = create_engine("sqlite://")
Session = sessionmaker(bind=engine)


if __name__ == "__main__":
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

test_a1 = A()
test_b1 = B(name="item_1", A=test_a1)
test_b2 = B(name="item_2", A=test_a1)
test_b3 = B(name="item_3", A=test_a1)

test_a2 = A()
test_b4 = B(name="item_4", A=test_a2)
test_b5 = B(name="item_5", A=test_a2)

with Session() as session:
    session.add_all([test_a1, test_a2])
    session.commit()

with Session() as session:
    pass
