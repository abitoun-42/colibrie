whl:
	poetry build -f wheel
	@mkdir -p whl
	@mv dist/*.whl whl/

.PHONY: whl 