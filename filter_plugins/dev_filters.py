# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError

def dev_expand(device, **kwargs):
    """Expand special file dictionary according to the list of placeholders.

    Keyword arguments:
    device -- dict with the special file attributes

    The return value will be a list of special file dictionaries as result of
    replacing the placeholders with the specified values.

    """
    # Prepare an empty result list structure

    result = list()
    for i in range(dev_placeholders_len(kwargs)):
        result.append(dict())

    # Fill the stcuture created in previous step with the expanded values

    for key, value in device.items():
        expanded_value = dev_expand_string(value, **kwargs)
        for i in range(len(expanded_value)):
            result[i][key] = expanded_value[i]

    return(result)


def dev_expand_string(string, **kwargs):
    """Expand an string according to a set of placeholders and values.

    Keyword arguments:
    string -- string to expand with placeholders using this format:

              {placeholder_name}

    **kwargs -- list of values to expand each placeholder.

    The return value will be a list of strings replacing the placeholders with
    the specified values.
    """
    if not kwargs:
        expanded_values = [ string ]
    else:
        expanded_values = list()
        format_args = list()
        size = dev_placeholders_len(kwargs)

        for key in kwargs:
            for i in range(size):
                if i >= len(format_args):
                    format_args.append({ key: kwargs[key][i] })
                else:
                    format_args[i].update({ key: kwargs[key][i] })

        for i in range(size):
            formatted_value = str(string).format(**format_args[i])
            expanded_values.append(formatted_value)

    return expanded_values

def dev_placeholders_len(placeholders):
    """Return the size of the placeholders values.

    Keyword arguments:
    placeholders -- dict with the following structure:
                    { 'placeholder_name_1': [ values_for_1 ],
                      'placeholder_name_n': [ values_for_n ]}

    The function returns the size of the placeholders values lists, that should
    be the same for all placeholders or an AnsibleFilterError exception will be
    raised,
    """
    size = None
    for key in placeholders:
        if size and size != len(placeholders[key]):
            raise AnsibleFilterError(
                'Placeholder lists must have the same size ('
                    + str(placeholders) + ')')
        else:
            size = len(placeholders[key])
    return size

def dev_to(start, end, step=1):
    """Return a list of integers.

    Keyword arguments:
    start -- beginning of the integer sequence.
    end   -- end of the integer sequence.
    step  -- step to jump between integers of the sequence.

    Note that both extremes (start and end) are included on the returned
    sequence.

    """
    return range(start, end + 1, step)

class FilterModule(object):
    """Ansible be_dell filters"""

    def filters(self):
        return {
            'dev_expand': dev_expand,
            'dev_to': dev_to,
        }
