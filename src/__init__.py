from src.main import Main
from .utils.constant import APIURLJSON, APIURLCSV
from .interface import EmpresaExtractInterface,EmpresaLoadInterface,EmpresaTransformCsvInterface,EmpresaTransformJsonInterface
from .etl import EmpresaExtract
from .utils import separatorJson