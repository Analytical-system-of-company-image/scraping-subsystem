poetry shell
rm -rf dist/
poetry build
export $(cat .env)
twine upload -u ${PYPI_TEST_USER} -p ${PYPI_TEST_PASWD} --repository pypi dist/*
