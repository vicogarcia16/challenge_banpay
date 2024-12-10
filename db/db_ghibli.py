from httpx import AsyncClient
from schemas.user import RoleEnum
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

async def get_ghibli_data(role: RoleEnum):
    if role == RoleEnum.admin:
        combined_data = {"admin": {}}
        async with AsyncClient() as client:
            for sub_role in RoleEnum:
                if sub_role == RoleEnum.admin:
                    continue
                response = await client.get(f"{BASE_URL}/{sub_role.value}")
                if response.status_code == 200:
                    combined_data["admin"][sub_role.value] = response.json()
                else:
                    combined_data["admin"][sub_role.value] = {
                        "error": f"Error al obtener los datos de {sub_role.value}"
                    }
        return combined_data
    else:
        async with AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/{role.value}")
            if response.status_code == 200:
                return {role.value: response.json()}
            else:
                return {role.value: {"error": f"Error al obtener los datos de {role.value}"}}
