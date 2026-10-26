import molotov
 
@molotov.scenario(weight=100)
async def test_server_json_200(session):
    async with session.get("http://localhost:3141/") as response:
        assert response.status == 200, f"Очікувався статус 200, отримано {response.status}"
 
        data = await response.json()
        assert isinstance(data, dict), "Тіло відповіді не є JSON-об'єктом"
