import pytest


@pytest.fixture(scope="session")
def tmp_fixture(tmp_path_factory):
    tmp_path = tmp_path_factory.mktemp("user_data")
    tmp_file = tmp_path / "test_user_data.txt"
    tmp_file.write_text("Hola mundo !")
    yield tmp_file


def test_upload_successful(client, tmp_fixture):
    with tmp_fixture.open("rb") as f:
        response = client.post(
            "/user/123/file",
            files={"file": ("test.txt", f, "text/plain")}
        )

    assert response.status_code == 200


def test_upload_has_expected_response(client, tmp_fixture):
    with tmp_fixture.open("rb") as f:
        response = client.post(
            "/user/123/file",
            files={"file": ("test.txt", f, "text/plain")}
        )

    json_resp = response.json()
    assert json_resp["user_id"] == 123
    assert json_resp["filename"] == "test.txt"
    assert json_resp["content"] == "Hola mundo !"
