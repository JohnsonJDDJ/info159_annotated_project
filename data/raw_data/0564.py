#!/usr/bin/env python

# Copyright 2021 Google LLC
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

import argparse


# [START secretmanager_update_secret_with_etag]
def update_secret_with_etag(project_id, secret_id, etag):
    """
    Update the metadata about an existing secret, using etag.
    """

    # Import the Secret Manager client library.
    from google.cloud import secretmanager

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret.
    name = client.secret_path(project_id, secret_id)

    # Update the secret.
    secret = {"name": name, "labels": {"secretmanager": "rocks"}, "etag": etag}
    update_mask = {"paths": ["labels"]}
    response = client.update_secret(
        request={"secret": secret, "update_mask": update_mask}
    )

    # Print the new secret name.
    print("Updated secret: {}".format(response.name))
    # [END secretmanager_update_secret_with_etag]

    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("project_id", help="id of the GCP project")
    parser.add_argument("secret-id", required=True)
    parser.add_argument("etag", help="current etag of the secret")
    args = parser.parse_args()

    update_secret_with_etag(args.project_id, args.secret_id, args.etag)