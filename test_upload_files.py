import pytest
import sys

if __name__ == "__main__":
    sys.path.append("../../..")

from utils.saas_api.case_process.data_loader import DataLoader
from utils.saas_api.app_service import app_service
from scripts.saas.utils.assertion import status_assert

# .yml - valid
_data_upload_file = DataLoader.get_test_data("test_upload_files_for_testing.yml")


class TestSetupFiles(object):
    @pytest.mark.parametrize("case_id, case_param", _data_upload_file[0], ids=_data_upload_file[1])
    def test_upload_file(self, case_id, case_param, saas_upload_file_option):
        if saas_upload_file_option["need_to_upload"]:
            _test_upload_file(case_param)


def _test_upload_file(params: dict):
    resp = app_service.put_file(params["body"]["upload_url"], params["body"]["image"], params["body"]["image"].split(".")[-1].lower())
    status_assert(resp)
