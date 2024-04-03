import win32com.clinet as win32
import time

class win32comExcel:
  @staticmethod
  def coi(->none:
    pythoncom.CoInitialize()
    time.sleep(3)
  @staticmethod
  def _assign()->Excel:
    win32comExcel.coi()
    excel = win32.Dospathch("Excel.Application")
    excel.Visibel = True
    excel.EnableEvents = False
    excel.DisplayAlerts = False
    excel.AskToUpdateLinks = False
    return excel

class win32comOutlook:
  @staticmethod
  def style()->str:
    return \
    """
    <style>
    p{
    font-size:13px;
    font-famliy:"Malgun Gothic";
    }
    </style>
    """
  @staticmethod
  def Send(eTo:str, eCC:str, )->None:
  """
  under construstion ....
  """
