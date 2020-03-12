from django.urls import reverse


class TestLoadAverage:
    def test_load_average_success(self, auth_user):
        url = reverse('supervisor:load-average')
        client, user = auth_user()
        resp = client.get(url)
        assert resp.status_code == 200
        assert b'1 min' in resp.content

    def test_load_average_not_authenticated(self, client):
        url = reverse('supervisor:load-average')
        resp = client.get(url)
        assert resp.status_code == 302
        # print(resp.headers)


class TestRam:
    def test_ram_success(self, auth_user):
        url = reverse('supervisor:ram')
        client, user = auth_user()
        resp = client.get(url)
        assert resp.status_code == 200

    def test_ram_not_authenticated(self, client):
        url = reverse('supervisor:ram')
        resp = client.get(url)
        assert resp.status_code == 302
