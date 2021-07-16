# Malaysia COVID-19 Press Releases

This repository contains all press release documents related to COVID-19 obtained from [Desk of DG Malaysia](https://kpkesihatan.com/) and their scraping scripts.

## Usage
You can retrieve the latest monthly archive files through the Releases tab.

The Python scripts uses the following packages: requests, bs4 and tqdm (which can be installed through requirements.txt)

`get_press.py` retrieve press releases from the `currprog.txt` file's date up till yesterday when the script is runned. `get_press_threading.py` uses threading to retrieve pres releases from 2020/01/06 (which can be configured in the file) up till now.

## License
The Python scripts are licensed under [MIT](LICENSE) while the press releases are all under copyright of Ministry of Health of Malaysia.
