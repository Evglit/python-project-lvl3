"""Module for loading page resources."""

import os
import logging
import requests
from progress.bar import Bar
from urllib.parse import urlparse, urljoin
from page_loader.names import get_name_resource
from page_loader.web_requests import get_web_resource


logger = logging.getLogger(__name__)


def is_local_url(attr_value, base_url):
    """Check url for locality."""
    netloc_attr = urlparse(attr_value).netloc
    netloc_base = urlparse(base_url).netloc
    if netloc_attr == '' or netloc_attr == netloc_base:
        return True
    return False


def find_resources(page_soup, resource_dir_path, base_url, resources):
    """Find the page resources to download."""
    tags = resources.keys()
    resource_tags = page_soup.find_all(tags)

    resources_for_download = []
    tags_for_change = []

    for resource_tag in resource_tags:
        attribute = resources[resource_tag.name]
        attr_value = resource_tag.get(attribute)

        if not is_local_url(attr_value, base_url):
            continue

        resource_url = urljoin(base_url, attr_value).rstrip('/')
        resource_name = get_name_resource(resource_url)
        resource_path = os.path.join(resource_dir_path, resource_name)
        new_attr_value = os.path.join(
            os.path.basename(resource_dir_path), resource_name)

        resources_for_download.append(
            {
                'resource_url': resource_url,
                'resource_path': resource_path
            }
        )
        tags_for_change.append(
            {
                'tag': resource_tag.name,
                'attribute': attribute,
                'old_attr_value': attr_value,
                'new_attr_value': new_attr_value
            }
        )

    return resources_for_download, tags_for_change


def download_resources(resources_for_download):
    """Download resources of page at the specified path."""
    logger.debug('Start downloading page resources.')
    bar = Bar('Loading page resources', max=len(resources_for_download))
    for resource in resources_for_download:
        try:
            get_web_resource(
                resource['resource_url'], resource['resource_path'])
            bar.next()
        except requests.exceptions.RequestException:
            logger.warning(
                f"Resource {resource['resource_url']} has not been downloaded.")
    bar.finish()
