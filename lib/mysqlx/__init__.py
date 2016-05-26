# MySQL Connector/Python - MySQL driver written in Python.
# Copyright (c) 2016, Oracle and/or its affiliates. All rights reserved.

# MySQL Connector/Python is licensed under the terms of the GPLv2
# <http://www.gnu.org/licenses/old-licenses/gpl-2.0.html>, like most
# MySQL Connectors. There are special exceptions to the terms and
# conditions of the GPLv2 as it is applied to this software, see the
# FOSS License Exception
# <http://www.mysql.com/about/legal/licensing/foss-exception.html>.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

"""MySQLx DevAPI Python implementation"""

from .connection import XSession, NodeSession
from .crud import Schema, Collection, Table
from .result import ColumnMetaData, Row, Result, BufferingResult, RowResult, SqlResult
from .statement import (DbDoc, Statement, FilterableStatement, SqlStatement,
                        AddStatement, RemoveStatement, TableDeleteStatement)


def get_session(settings):
    return XSession(settings)


def get_node_session(settings):
    return NodeSession(settings)

__all__ = [
    # mysqlx.connection
    XSession, NodeSession, get_session, get_node_session,

    # mysqlx.crud
    Schema, Collection, Table,

    # mysqlx.result
    ColumnMetaData, Row, Result, BufferingResult, RowResult, SqlResult,

    # mysqlx.statement
    DbDoc, Statement, FilterableStatement, SqlStatement, AddStatement,
    RemoveStatement, TableDeleteStatement,
]
