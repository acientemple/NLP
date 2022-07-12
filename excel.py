#!/usr/bin/python
# coding=utf-8
__author__ = 'Paul'

import xlrd
import chardet
import traceback


def getColumnIndex(table, columnName):
    columnIndex = None
    # print table
    for i in range(table.ncols):
        # print columnName
        # print table.cell_value(0, i)
        if (table.cell_value(0, i) == columnName):
            columnIndex = i
            break
    return (columnIndex)


def readExcelDataByName(fileName, sheetName):
        data = xlrd.open_workbook(fileName,'rb')
        table = data.sheet_by_name(sheetName)
        return (table)


table = readExcelDataByName('2021_1.xls', 'zhejiang')
# 获取第一行的值
shool_code = table.cell_value(2, getColumnIndex(table, 'school_code'))
entry_score = table.cell_value(2, getColumnIndex(table, 'entry_score'))

print (shool_code)
print (entry_score)