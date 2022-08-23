from datetime import datetime
from unittest import TestCase
from unittest.mock import patch

import schemas.provider as schemas
from repositories.providers import update_provider, create_provider


class MethodTest(TestCase):

    @patch('repositories.providers.get_provider')
    def test_update_provider_not_exist(self, get_provider_mock):
        get_provider_mock.return_value = None
        provider_schema = schemas.Provider(
            id="mock",
            name="mock",
            company="mock",
            created_at=datetime.now(),
            amount_products=0
        )
        result = update_provider(None, "123", provider_schema)
        get_provider_mock.assert_called_once()
        assert result is None

    @patch('sqlalchemy.orm.Session')
    def test_create_provider(self, session_mock):
        provider_schema = schemas.Provider(
            id="mock",
            name="mock",
            company="mock",
            created_at=datetime.now(),
            amount_products=0
        )
        result = create_provider(session_mock, provider_schema)

        assert result.id == provider_schema.id
        assert result.name == provider_schema.name
        assert result.company == provider_schema.company
        assert result.created_at == provider_schema.created_at
        assert result.amount_products == provider_schema.amount_products
