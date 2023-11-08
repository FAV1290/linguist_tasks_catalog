import decimal
import requests


def fetch_exchanger_response() -> requests.Response:
    url = 'https://dram.am/direct/noncash'
    headers = {'User-Agent': 'Mozilla/5.0'}
    return requests.get(url=url, headers=headers)


def create_substrings_pair_internal_slice(
    initial_string: str,
    first_substring: str,
    second_substring: str,
) -> str:
    start_index = initial_string.find(first_substring) + len(first_substring)
    end_index = initial_string.find(second_substring, start_index)
    return initial_string[start_index:end_index]


def calculate_usd_to_rur_rate() -> decimal.Decimal:
    response = fetch_exchanger_response()
    target_row_slice = create_substrings_pair_internal_slice(
        response.text, '/bank/9', '<div class="table-item eleven">')
    usd_to_amd_rate_slice = create_substrings_pair_internal_slice(
        target_row_slice, '<div class="table-item four">', '</div>')
    usd_to_amd_rate = decimal.Decimal(create_substrings_pair_internal_slice(
        usd_to_amd_rate_slice, 'data-price="', '"'))
    amd_to_rur_rate_slice = create_substrings_pair_internal_slice(
        target_row_slice, '<div class="table-item nine">', '</div>')
    amd_to_rur_rate = decimal.Decimal(create_substrings_pair_internal_slice(
        amd_to_rur_rate_slice, 'data-price="', '"'))
    amd_to_usd_rate = usd_to_amd_rate / amd_to_rur_rate
    return amd_to_usd_rate
