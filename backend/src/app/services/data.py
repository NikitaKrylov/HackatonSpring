from io import BytesIO

import pandas as pd
from fastapi import HTTPException, status

engines = {
        '.xlsx': 'openpyxl',
        '.xls': 'xlrd'
    }

async def bytes_to_pandas(data: bytes, file_extension: str):
    io = BytesIO(data)

    if file_extension == '.csv':
        return pd.read_csv(io)

    if file_extension not in engines:
        raise HTTPException(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, f'Файлы с расширением {file_extension} не поддерживаются')

    return pd.read_excel(io, engine=engines[file_extension])


async def bytes_to_dict(data: bytes):
    # TODO сделать конвертацию json(bytes) в dict
    pass
