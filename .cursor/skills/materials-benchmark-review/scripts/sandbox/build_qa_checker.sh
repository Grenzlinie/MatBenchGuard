#!/usr/bin/env bash
#
# Build the preconfigured checker image once before running Review or Repair.
#
# Default:
#   docker build -f .cursor/skills/materials-benchmark-review/scripts/sandbox/Dockerfile \
#     -t qa-checker:1.0 \
#     .cursor/skills/materials-benchmark-review/scripts/sandbox
#
# Override the tag with MATERIALS_CHECKER_IMAGE_TAG (or
# MATERIALS_CHECKER_IMAGE) when maintaining a separate local image version.

set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
image_tag="${MATERIALS_CHECKER_IMAGE_TAG:-${MATERIALS_CHECKER_IMAGE:-qa-checker:1.0}}"

exec docker build \
  -f "${script_dir}/Dockerfile" \
  -t "${image_tag}" \
  "${script_dir}"
