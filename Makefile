main-run:
	docker-compose up

main-start:
	docker-compose up --build

main-stop:
	docker-compose down

web-run:
	docker-compose -f docker-compose-web.yaml up

web-start:
	docker-compose -f docker-compose-web.yaml up --build

web-stop:
	docker-compose -f docker-compose-web.yaml down