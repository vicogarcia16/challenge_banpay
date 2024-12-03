import requests
from schemas.user import RoleEnum
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def get_ghibli_data(role: RoleEnum):
    if role == RoleEnum.admin:
        combined_data = {"admin": {}}
        for sub_role in RoleEnum:
            if sub_role == RoleEnum.admin:
                continue
            response = requests.get(f"{BASE_URL}/{sub_role.value}")
            if response.status_code == 200:
                combined_data["admin"][sub_role.value] = response.json()
            else:
                combined_data["admin"][sub_role.value] = {
                    "error": f"Error al obtener los datos de {sub_role.value}"
                }
        return combined_data
    else:
        response = requests.get(f"{BASE_URL}/{role.value}")
        if response.status_code == 200:
            return {role.value: response.json()}
        else:
            return {role.value: {"error": f"Error al obtener los datos de {role.value}"}}
