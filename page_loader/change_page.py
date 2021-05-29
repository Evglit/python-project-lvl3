"""The module contains functions for changing the content of the page"""

import logging


logger = logging.getLogger(__name__)


def replace_res_path(page_soup, tags_for_change):
    """Replace old page resource paths with new ones."""
    logger.debug("Replace old page resource paths with new ones")
    for tag_for_change in tags_for_change:
        old_tag = page_soup.find(
            tag_for_change['tag'],
            {tag_for_change['attribute']: tag_for_change['old_attr_value']}
        )
        old_tag[tag_for_change['attribute']] = tag_for_change['new_attr_value']
    return page_soup
