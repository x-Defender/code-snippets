# please Pray For Palestine  🥺♥️
#
#
#
#
#
# aut: [r00tk1t]
# processing ,
# private => cwd => config ,
# cuckoo  => web => templates > analysis => pages => static => _yourfile.html
# cuckoo  => web => templates > analysis => pages => static => index.html
# cuckoo  => common => config.py
# files   => 1.capa_processing.py
#         => 2._capa.html
#         => 3.index.html
#         => 4.common/config.py
#         => 5.cwd/config/processing.conf
#         => 6.home/conf/processing.conf

import os.path
# import re
import subprocess
from cuckoo.common.abstracts import Processing
from cuckoo.common.exceptions import CuckooProcessingError


class Capa(Processing):
    """Extract Capa Signatures from analyzed file."""

    def run(self):
        """Run capa extractor .
        @return: list of rules strings.
        """
        self.key = "capa_res"
        results = []

        self.capa = self.options.get("capa", "/usr/local/bin/capa")

        # if self.task["category"] == "file":
        #     if not os.path.exists(self.file_path):
        #         raise CuckooProcessingError(
        #             "Sample file doesn't exist: \"%s\"" % self.file_path
        #         )

        if not os.path.exists(self.file_path):
            raise CuckooProcessingError(
                "Sample file doesn't exist: \"%s\"" % self.file_path
            )

        if not os.path.isfile(self.capa):
            raise CuckooProcessingError("Unable to locate Capa binary")

        args = [
            self.capa,
            self.file_path,
        ]

        try:
            output = subprocess.check_output(args)
        except subprocess.CalledProcessError as e:
            raise CuckooProcessingError(
                "Capa returned an error processing this sample: %s" % e)

        for line in output.split("\n"):
            if not line:
                continue
            else:
                results.append(line)
        return results
