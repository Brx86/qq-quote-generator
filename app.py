from base64 import encodebytes
from pathlib import Path
from typing import Literal

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response
from jinja2 import Environment, FileSystemLoader

from ascreenshot import screenshot

app = FastAPI(docs_url=None)
app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
template = Environment(
    loader=FileSystemLoader(Path(__file__).parent / "templates"),
    enable_async=True,
).get_template("main-template.html")


@app.get("/")
def read_root() -> JSONResponse:
    return JSONResponse({"Github": "https://github.com/Brx86/qq-quote-generator"})


@app.post(path="/{r_type}")
async def handler(
    data_list: list[dict],
    r_type: Literal["jpeg", "png", "base64"],
) -> Response:
    """处理post请求，返回图片数据

    Args:
        data_list (list[dict]): 消息数据
        r_type (Literal["jpeg", "png", "base64"]): 图片形式

    Returns:
        Response: 图片的base64或文件bytes
    """
    html = await template.render_async(data_list=data_list)
    if r_type == "base64":
        return Response(encodebytes(await screenshot(html=html, locate="#app")))
    return Response(await screenshot(html=html, locate="#app", type=r_type))
