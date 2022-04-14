# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for DeleteLogMetric
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-logging


# [START logging_v2_generated_MetricsServiceV2_DeleteLogMetric_sync_6f5ac8ec]
from google.cloud import logging_v2


def sample_delete_log_metric():
    # Create a client
    client = logging_v2.MetricsServiceV2Client()

    # Initialize request argument(s)
    request = logging_v2.DeleteLogMetricRequest(
        metric_name="metric_name_value",
    )

    # Make the request
    client.delete_log_metric(request=request)


# [END logging_v2_generated_MetricsServiceV2_DeleteLogMetric_sync_6f5ac8ec]