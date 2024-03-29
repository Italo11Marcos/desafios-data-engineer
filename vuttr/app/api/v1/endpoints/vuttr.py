from fastapi import Depends, HTTPException, status, Response, APIRouter, Query, Body
from sqlalchemy import Select
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from models import VuttrModel, TagModel
from database import get_session


router = APIRouter()
@router.post('/tools', response_model=dict, status_code=201)
def read_tools(tools: dict = Body(
                example={
                        "title": "hotel",
                        "link": "https://github.com/typicode/hotel",
                        "description": "Local app manager. Start apps within your browser, developer tool with local .localhost domain and https out of the box.",
                        "tags":["node", "organizing", "webapps", "domain", "developer", "https", "proxy"]
                    }
            ), 
            db: Session = Depends(get_session)):
    full_tools = tools.copy()
    tags_data = tools.pop('tags')
    db_tools = VuttrModel(**tools)
    db.add(db_tools)
    with db as session:
        db.merge(db_tools)
        for tg in tags_data:
            query = Select(TagModel).filter(TagModel.nome == tg)
            result = session.execute(query)
            exists_tag = result.scalar_one_or_none()
            db_tags = TagModel(nome=tg)
            if exists_tag:
                db_tools.tags.append(exists_tag)
            else:
                db.add(db_tags)
                db_tools.tags.append(db_tags)
        db.commit()

    return full_tools


@router.get('/tools', response_model=dict, status_code=200)
def read_tools(db: Session = Depends(get_session)):
    with db as session:
        query = """
            select
            v.id,
            v.title,
            v.link,
            v.description,
            t.nome as tag
            from vuttrs v
            join vuttr_tag vt on vt.vuttr_id = v.id
            join tags t on t.id = vt.tag_id
        """
        result = session.execute(text(query))
        
        # Converter objetos em formato JSON
        json_objects = []
        for r in result:
            json_obj = {
                "id": r.id,
                "title": r.title,
                "link": r.link,
                "description": r.description,
                "tags": [r.tag]
            }
            json_objects.append(json_obj)

        # Agrupar os objetos pelo id
        grouped_json_objects = {}
        for obj in json_objects:
            if obj["id"] not in grouped_json_objects:
                grouped_json_objects[obj["id"]] = {
                    "id": obj["id"],
                    "title": obj["title"],
                    "link": obj["link"],
                    "description": obj["description"],
                    "tags": obj["tags"]
                }
            else:
                grouped_json_objects[obj["id"]]["tags"].extend(obj["tags"])
        # Converter para uma lista de valores no dicionário
        final_json = list(grouped_json_objects.values())
    return {'tools': final_json}


@router.get('/tools/', response_model=dict, status_code=200)
def read_tool(tag: str = Query(), db: Session = Depends(get_session)):
    with db as session:
        query = f"""
            with cte_tags as (
                select
                vt.vuttr_id as id
                from tags t 
                join vuttr_tag vt on t.id = vt.tag_id
                where t.nome = '{tag}'
            )
            select
            v.id,
            v.title,
            v.link,
            v.description,
            t.nome as tag
            from vuttrs v
            join vuttr_tag vt on vt.vuttr_id = v.id
            join tags t on t.id = vt.tag_id 
            join cte_tags ct on ct.id = v.id
        """
        result = session.execute(text(query))
        # Converter objetos em formato JSON
        json_objects = []
        for r in result:
            json_obj = {
                "id": r.id,
                "title": r.title,
                "link": r.link,
                "description": r.description,
                "tags": [r.tag]
            }
            json_objects.append(json_obj)

        # Agrupar os objetos pelo id
        grouped_json_objects = {}
        for obj in json_objects:
            if obj["id"] not in grouped_json_objects:
                grouped_json_objects[obj["id"]] = {
                    "id": obj["id"],
                    "title": obj["title"],
                    "link": obj["link"],
                    "description": obj["description"],
                    "tags": obj["tags"]
                }
            else:
                grouped_json_objects[obj["id"]]["tags"].extend(obj["tags"])
        # Converter para uma lista de valores no dicionário
        final_json = list(grouped_json_objects.values())
    return {'tools': final_json}


@router.delete('/tools/{tool_id}', response_model=dict, status_code=200)
def read_tool(tool_id: int, db: Session = Depends(get_session)):
    with db as session:
        query = Select(VuttrModel).filter(VuttrModel.id == tool_id)
        result = session.execute(query)
        tool_del = result.scalar_one_or_none()
        if tool_del:
            session.delete(tool_del)
            session.commit()
            return {}
        else:
            raise HTTPException(detail='Tool not found',
                                status_code=status.HTTP_404_NOT_FOUND)


@router.get('/tags', response_model=dict , status_code=200)
def read_tools(db: Session = Depends(get_session)):
    with db as session:
        query = """
            select 
            nome
            from tags
        """
        result = session.execute(text(query))
        tags = [r[0] for r in result]
        print(tags)
    return {'tags': tags}