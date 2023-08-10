# coding: utf-8
from sqlalchemy import CheckConstraint, Column, DECIMAL, Date, DateTime, ForeignKey, Index, Integer, SmallInteger, String, Text
from sqlalchemy.dialects.mysql import MEDIUMBLOB, MEDIUMTEXT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  August 08, 2023 13:27:28
# Database: mysql+pymysql://root:p@localhost:3306/classicmodels
# Dialect:  mysql
#
# mypy: ignore-errors
########################################################################################################################

from safrs import SAFRSBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.mysql import *



class AbPermission(SAFRSBase, Base):
    __tablename__ = 'ab_permission'
    _s_collection_name = 'AbPermission'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    # parent relationships (access parent)

    # child relationships (access children)
    AbPermissionViewList : Mapped[List["AbPermissionView"]] = relationship(back_populates="permission")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class AbRegisterUser(SAFRSBase, Base):
    __tablename__ = 'ab_register_user'
    _s_collection_name = 'AbRegisterUser'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False, unique=True)
    password = Column(String(256))
    email = Column(String(64), nullable=False)
    registration_date = Column(DateTime)
    registration_hash = Column(String(256))

    # parent relationships (access parent)

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class AbRole(SAFRSBase, Base):
    __tablename__ = 'ab_role'
    _s_collection_name = 'AbRole'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, unique=True)

    # parent relationships (access parent)

    # child relationships (access children)
    AbUserRoleList : Mapped[List["AbUserRole"]] = relationship(back_populates="role")
    AbPermissionViewRoleList : Mapped[List["AbPermissionViewRole"]] = relationship(back_populates="role")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class AbUser(SAFRSBase, Base):
    __tablename__ = 'ab_user'
    _s_collection_name = 'AbUser'  # type: ignore
    __bind_key__ = 'None'
    __table_args__ = (
        CheckConstraint('(`active` in (0,1))'),
    )

    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False, unique=True)
    password = Column(String(256))
    active = Column(TINYINT(1))
    email = Column(String(64), nullable=False, unique=True)
    last_login = Column(DateTime)
    login_count = Column(Integer)
    fail_login_count = Column(Integer)
    created_on = Column(DateTime)
    changed_on = Column(DateTime)
    created_by_fk = Column(ForeignKey('ab_user.id'), index=True)
    changed_by_fk = Column(ForeignKey('ab_user.id'), index=True)

    # parent relationships (access parent)
    AbUser : Mapped["AbUser"] = relationship(foreign_keys='[AbUser.changed_by_fk]', remote_side=[id], back_populates=("AbUserList"))
    AbUser1 : Mapped["AbUser"] = relationship(foreign_keys='[AbUser.created_by_fk]', remote_side=[id], back_populates=("AbUserList1"))

    # child relationships (access children)
    AbUserList : Mapped[List["AbUser"]] = relationship(foreign_keys='[AbUser.changed_by_fk]', back_populates="AbUser")
    AbUserList1 : Mapped[List["AbUser"]] = relationship(foreign_keys='[AbUser.created_by_fk]', back_populates="AbUser1")
    AbUserRoleList : Mapped[List["AbUserRole"]] = relationship(back_populates="user")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class AbViewMenu(SAFRSBase, Base):
    __tablename__ = 'ab_view_menu'
    _s_collection_name = 'AbViewMenu'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)

    # parent relationships (access parent)

    # child relationships (access children)
    AbPermissionViewList : Mapped[List["AbPermissionView"]] = relationship(back_populates="view_menu")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Office(SAFRSBase, Base):
    __tablename__ = 'offices'
    _s_collection_name = 'Office'  # type: ignore
    __bind_key__ = 'None'

    officeCode = Column(String(10), primary_key=True)
    city = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    addressLine1 = Column(String(50), nullable=False)
    addressLine2 = Column(String(50))
    state = Column(String(50))
    country = Column(String(50), nullable=False)
    postalCode = Column(String(15), nullable=False)
    territory = Column(String(10), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    EmployeeList : Mapped[List["Employee"]] = relationship(back_populates="office")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Productline(SAFRSBase, Base):
    __tablename__ = 'productlines'
    _s_collection_name = 'Productline'  # type: ignore
    __bind_key__ = 'None'

    productLine = Column(String(50), primary_key=True)
    textDescription = Column(String(4000))
    htmlDescription = Column(MEDIUMTEXT)
    image = Column(MEDIUMBLOB)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    ProductList : Mapped[List["Product"]] = relationship(back_populates="productline")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class AbPermissionView(SAFRSBase, Base):
    __tablename__ = 'ab_permission_view'
    _s_collection_name = 'AbPermissionView'  # type: ignore
    __bind_key__ = 'None'
    __table_args__ = (
        Index('permission_id', 'permission_id', 'view_menu_id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    permission_id = Column(ForeignKey('ab_permission.id'))
    view_menu_id = Column(ForeignKey('ab_view_menu.id'), index=True)

    # parent relationships (access parent)
    permission : Mapped["AbPermission"] = relationship(back_populates=("AbPermissionViewList"))
    view_menu : Mapped["AbViewMenu"] = relationship(back_populates=("AbPermissionViewList"))

    # child relationships (access children)
    AbPermissionViewRoleList : Mapped[List["AbPermissionViewRole"]] = relationship(back_populates="permission_view")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class AbUserRole(SAFRSBase, Base):
    __tablename__ = 'ab_user_role'
    _s_collection_name = 'AbUserRole'  # type: ignore
    __bind_key__ = 'None'
    __table_args__ = (
        Index('user_id', 'user_id', 'role_id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('ab_user.id'))
    role_id = Column(ForeignKey('ab_role.id'), index=True)

    # parent relationships (access parent)
    role : Mapped["AbRole"] = relationship(back_populates=("AbUserRoleList"))
    user : Mapped["AbUser"] = relationship(back_populates=("AbUserRoleList"))

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Employee(SAFRSBase, Base):
    __tablename__ = 'employees'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    employeeNumber = Column(Integer, primary_key=True)
    lastName = Column(String(50), nullable=False)
    firstName = Column(String(50), nullable=False)
    extension = Column(String(10), nullable=False)
    email = Column(String(100), nullable=False)
    officeCode = Column(ForeignKey('offices.officeCode'), nullable=False, index=True)
    reportsTo = Column(ForeignKey('employees.employeeNumber'), index=True)
    jobTitle = Column(String(50), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    office : Mapped["Office"] = relationship(back_populates=("EmployeeList"))
    Employee : Mapped["Employee"] = relationship(remote_side=[employeeNumber], back_populates=("EmployeeList"))

    # child relationships (access children)
    EmployeeList : Mapped[List["Employee"]] = relationship(back_populates="Employee")
    CustomerList : Mapped[List["Customer"]] = relationship(back_populates="employee")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Product(SAFRSBase, Base):
    __tablename__ = 'products'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    productCode = Column(String(15), primary_key=True)
    productName = Column(String(70), nullable=False)
    productLine = Column(ForeignKey('productlines.productLine'), nullable=False, index=True)
    productScale = Column(String(10), nullable=False)
    productVendor = Column(String(50), nullable=False)
    productDescription = Column(Text, nullable=False)
    quantityInStock = Column(SmallInteger, nullable=False)
    buyPrice : DECIMAL = Column(DECIMAL(10, 2), nullable=False)
    MSRP : DECIMAL = Column(DECIMAL(10, 2), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    productline : Mapped["Productline"] = relationship(back_populates=("ProductList"))

    # child relationships (access children)
    OrderdetailList : Mapped[List["Orderdetail"]] = relationship(back_populates="product")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class AbPermissionViewRole(SAFRSBase, Base):
    __tablename__ = 'ab_permission_view_role'
    _s_collection_name = 'AbPermissionViewRole'  # type: ignore
    __bind_key__ = 'None'
    __table_args__ = (
        Index('permission_view_id', 'permission_view_id', 'role_id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    permission_view_id = Column(ForeignKey('ab_permission_view.id'))
    role_id = Column(ForeignKey('ab_role.id'), index=True)

    # parent relationships (access parent)
    permission_view : Mapped["AbPermissionView"] = relationship(back_populates=("AbPermissionViewRoleList"))
    role : Mapped["AbRole"] = relationship(back_populates=("AbPermissionViewRoleList"))

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Customer(SAFRSBase, Base):
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    customerNumber = Column(Integer, primary_key=True)
    customerName = Column(String(50), nullable=False)
    contactLastName = Column(String(50), nullable=False)
    contactFirstName = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    addressLine1 = Column(String(50), nullable=False)
    addressLine2 = Column(String(50))
    city = Column(String(50), nullable=False)
    state = Column(String(50))
    postalCode = Column(String(15))
    country = Column(String(50), nullable=False)
    salesRepEmployeeNumber = Column(ForeignKey('employees.employeeNumber'), index=True)
    creditLimit : DECIMAL = Column(DECIMAL(10, 2))
    allow_client_generated_ids = True

    # parent relationships (access parent)
    employee : Mapped["Employee"] = relationship(back_populates=("CustomerList"))

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="customer")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Order(SAFRSBase, Base):
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    orderNumber = Column(Integer, primary_key=True)
    orderDate = Column(Date, nullable=False)
    requiredDate = Column(Date, nullable=False)
    shippedDate = Column(Date)
    status = Column(String(15), nullable=False)
    comments = Column(Text)
    customerNumber = Column(ForeignKey('customers.customerNumber'), nullable=False, index=True)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderdetailList : Mapped[List["Orderdetail"]] = relationship(back_populates="order")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Payment(SAFRSBase, Base):
    __tablename__ = 'payments'
    _s_collection_name = 'Payment'  # type: ignore
    __bind_key__ = 'None'

    customerNumber = Column(ForeignKey('customers.customerNumber'), primary_key=True, nullable=False)
    checkNumber = Column(String(50), primary_key=True, nullable=False)
    paymentDate = Column(Date, nullable=False)
    amount : DECIMAL = Column(DECIMAL(10, 2), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("PaymentList"))

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Orderdetail(SAFRSBase, Base):
    __tablename__ = 'orderdetails'
    _s_collection_name = 'Orderdetail'  # type: ignore
    __bind_key__ = 'None'

    orderNumber = Column(ForeignKey('orders.orderNumber'), primary_key=True, nullable=False)
    productCode = Column(ForeignKey('products.productCode'), primary_key=True, nullable=False, index=True)
    quantityOrdered = Column(Integer, nullable=False)
    priceEach : DECIMAL = Column(DECIMAL(10, 2), nullable=False)
    orderLineNumber = Column(SmallInteger, nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderdetailList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderdetailList"))

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_
