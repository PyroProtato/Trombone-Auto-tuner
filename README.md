# Trombone Autotuner

![IMG_3203](https://github.com/user-attachments/assets/81595d10-a649-4f2f-b6ec-d6a3e1b2bff0)

Hello! This is my first big personal hardware project. It's a custom autotuner for the Trombone! It should be able to detect whether the user is flat or sharp when playing a note and adjust the tuning slide to fit the pitch better.

I made this project because I want to get better at the hardware side of personal projects. I have been doing a lot of coding and game design in my free time, and I want to venture outside of my confort zone. I already know I have the skills necessary from my time in FRC robotics, so I want to make my own ideas come to life! This is one of those ideas that I had since I also enjoy playing the trombone and also I'm not the best at tuning :P

This is compatible specifically with the Yamaha Allegro Trombone with F Attachment

![Screenshot 2025-12-29 162556](https://github.com/user-attachments/assets/381292a7-dae7-447e-95c0-ecc16ca436f5)

BOM (commercial products):
| Part | Amount | Price | Link |
| --- | --- | --- | --- |
| Linear Actuators | 2x | ~$48 | [https://www.digikey.com/en/products/detail/dfrobot/FIT0803/14824998](https://www.digikey.com/en/products/detail/dfrobot/FIT0803/14824998) |
| M3 Heatset Insert | 26x | $5.95 | [https://www.adafruit.com/product/4256?gad_source=1&gad_campaignid=21079227318&gbraid=0AAAAADx9JvQqarUxNuCSIE1qDs0R13337&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxJQlT_iRvEh3xS3mAPNyFk3gSaS8bFPCvhvamXXNOqIlSAQFgW5hyYaAnWJEALw_wcB](https://www.adafruit.com/product/4256?gad_source=1&gad_campaignid=21079227318&gbraid=0AAAAADx9JvQqarUxNuCSIE1qDs0R13337&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxJQlT_iRvEh3xS3mAPNyFk3gSaS8bFPCvhvamXXNOqIlSAQFgW5hyYaAnWJEALw_wcB) |
| M3 8mm bolts | 26x | $8.50 | [https://accu-components.com/us/metric-cap-head-screws/3818-SSCF-M3-8-A2?google_shopping=1&c=2&gad_source=1&gad_campaignid=23876758716&gbraid=0AAAAADI7_w40y8xg1d7LxsfQ-9SXwpZnK&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxJwLdjjRB3aRNg0EnVpm0exKA-6AZLaLQK3qjjKGWQY31yhfLE97VoaAhOcEALw_wcB](https://accu-components.com/us/metric-cap-head-screws/3818-SSCF-M3-8-A2?google_shopping=1&c=2&gad_source=1&gad_campaignid=23876758716&gbraid=0AAAAADI7_w40y8xg1d7LxsfQ-9SXwpZnK&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxJwLdjjRB3aRNg0EnVpm0exKA-6AZLaLQK3qjjKGWQY31yhfLE97VoaAhOcEALw_wcB) |
| M3 20mm bolts | 12x | $3.84 | [https://accu-components.com/us/metric-cap-head-screws/2802-SSC-M3-20-A2?google_shopping=1&c=2&gad_source=1&gad_campaignid=23876758716&gbraid=0AAAAADI7_w40y8xg1d7LxsfQ-9SXwpZnK&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxIP57iRP1C9n9sUTBfrwggPK11mbWwnx1p7wGkcPmdvGiXVzViDQb4aAgM6EALw_wcB](https://accu-components.com/us/metric-cap-head-screws/2802-SSC-M3-20-A2?google_shopping=1&c=2&gad_source=1&gad_campaignid=23876758716&gbraid=0AAAAADI7_w40y8xg1d7LxsfQ-9SXwpZnK&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxIP57iRP1C9n9sUTBfrwggPK11mbWwnx1p7wGkcPmdvGiXVzViDQb4aAgM6EALw_wcB) |
| M3 Hex Standoff | 8x | $3.57 | [https://ca.robotshop.com/products/m3-10mm-hex-standoff-mounting-kit-10pk](https://ca.robotshop.com/products/m3-10mm-hex-standoff-mounting-kit-10pk) |
| Arduino Uno | 1x | $30.88 | [https://everymarket.com/products/elegoo-uno-r3-control-board-usb-cable-for-arduino?utm_source=google&utm_medium=cpc&utm_campaign=23241618718&utm_content=194018747971&utm_term=&gad_source=1&gad_campaignid=23241618718&gbraid=0AAAAACe9t8bSJQNz7uj8Ixpx3ycu_pbMI&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxIfk4C7ij5PRFfjb0dXZ9I8I7pJ7SvRQjJiEXUeli1-AgBpccFkpRUaAhVqEALw_wcB](https://everymarket.com/products/elegoo-uno-r3-control-board-usb-cable-for-arduino?utm_source=google&utm_medium=cpc&utm_campaign=23241618718&utm_content=194018747971&utm_term=&gad_source=1&gad_campaignid=23241618718&gbraid=0AAAAACe9t8bSJQNz7uj8Ixpx3ycu_pbMI&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxIfk4C7ij5PRFfjb0dXZ9I8I7pJ7SvRQjJiEXUeli1-AgBpccFkpRUaAhVqEALw_wcB) |
| Duracell 9V Battery | 1x | $14.06 | [https://www.amazon.com/Duracell-Coppertop-Alkaline-Batteries-Count/dp/B000K2NW08?th=1](https://www.amazon.com/Duracell-Coppertop-Alkaline-Batteries-Count/dp/B000K2NW08?th=1) |
| L298N Motor Controller | 1x | $6.99 | [https://www.amazon.com/Qunqi-Controller-Module-Stepper-Arduino/dp/B014KMHSW6/ref=sr_1_6?dib=eyJ2IjoiMSJ9.hK2FjV8Ukp8CCyVTI1seMk4n3aguoO_lNXX3xoiH-O2cqubPGQBPAsy3IeO-_8qnficzzzC29kZvbL-1QjZry_X02KZdKgv249TdibwnicN5zbqpWVIQjaJkxD-4PPGW7ouVXHiiyqtmm69Aip82uAUNE1wg8hNuoww2e5m89eoqK6EDC9Z653jrEtQAsDUK5sM2BUX6HJw7bsusfliQ_zJj2DztUjH8Vsy-aCtZax0.TAwSBtHutxU8L5A34GuZh8UhVDyfs3kSvm88m7vmqbo&dib_tag=se&keywords=l298n&qid=1780447466&sr=8-6](https://www.amazon.com/Qunqi-Controller-Module-Stepper-Arduino/dp/B014KMHSW6/ref=sr_1_6?dib=eyJ2IjoiMSJ9.hK2FjV8Ukp8CCyVTI1seMk4n3aguoO_lNXX3xoiH-O2cqubPGQBPAsy3IeO-_8qnficzzzC29kZvbL-1QjZry_X02KZdKgv249TdibwnicN5zbqpWVIQjaJkxD-4PPGW7ouVXHiiyqtmm69Aip82uAUNE1wg8hNuoww2e5m89eoqK6EDC9Z653jrEtQAsDUK5sM2BUX6HJw7bsusfliQ_zJj2DztUjH8Vsy-aCtZax0.TAwSBtHutxU8L5A34GuZh8UhVDyfs3kSvm88m7vmqbo&dib_tag=se&keywords=l298n&qid=1780447466&sr=8-6) |
| Assorted Jumper Wires | ~10-12 | $6.98 | [https://www.amazon.com/Elegoo-EL-CP-004-Multicolored-Breadboard-arduino/dp/B01EV70C78/ref=sr_1_1_sspa?crid=14G2KXMONOP7R&dib=eyJ2IjoiMSJ9.QGbaFF62mgZ1Tf0J7CajkNBsnVj5R36wj-0pJgNimbPLS41NGdbYQRZJoCqqFZPke6kHd1goDWvYKePoebaUExzD0AEQXL6JJc1IrlrmqzgmRc6v697e4jJrZQHZEeQ62w_h8ceOiJSK1IQRo_nFSuvm8t-IW9kj9mdwEWKYSSVyzxl0y9zZ1zQsNl7pvw3HAr6kaEFNPYtGaGprygJk3VsUfBgkt1LX47rjjnW3vRA.ECeZMTeF7JSRkWDl0DeYkoOpjVorT5ZBlvaILqsRIuE&dib_tag=se&keywords=arduino+jumper+wires&qid=1780447537&sprefix=arduino+jumper+wires%2Caps%2C145&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1](https://www.amazon.com/Elegoo-EL-CP-004-Multicolored-Breadboard-arduino/dp/B01EV70C78/ref=sr_1_1_sspa?crid=14G2KXMONOP7R&dib=eyJ2IjoiMSJ9.QGbaFF62mgZ1Tf0J7CajkNBsnVj5R36wj-0pJgNimbPLS41NGdbYQRZJoCqqFZPke6kHd1goDWvYKePoebaUExzD0AEQXL6JJc1IrlrmqzgmRc6v697e4jJrZQHZEeQ62w_h8ceOiJSK1IQRo_nFSuvm8t-IW9kj9mdwEWKYSSVyzxl0y9zZ1zQsNl7pvw3HAr6kaEFNPYtGaGprygJk3VsUfBgkt1LX47rjjnW3vRA.ECeZMTeF7JSRkWDl0DeYkoOpjVorT5ZBlvaILqsRIuE&dib_tag=se&keywords=arduino+jumper+wires&qid=1780447537&sprefix=arduino+jumper+wires%2Caps%2C145&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1) |

BOM (3D Prints):
| Name | Amount |
| --- | --- |
| BottomHalf1 | 1x |
| BottomHalf2 | 1x |
| TopHalf1 | 1x |
| TopHalf2v2 | 1x |
| MotorMount | 2x |
| BottomMountTop | 2x |
| TopMotorMount | 2x |
| M3 Adapter | 2x |





