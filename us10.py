"""
Author: yzhou
"""


def us10_marriage_after_14(repo1):
    """ Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old). """

    error = []

    for fam in repo1.families.values():
        marriage_date = fam.repo['MARR']['detail']

        if marriage_date != 'NA':
            hus_id = fam.repo['HUSB']['detail']
            wife_id = fam.repo['WIFE']['detail']

            for indi in repo1.individuals.values():
                if indi.indi_id == hus_id:
                    hus_birth = indi.repo['BIRT']['detail']
                    if abs((marriage_date - hus_birth).days / 365.25) < 14:
                        error_message = f'Husband:<{indi.indi_id}> marriage before he is 14 years old.'
                        error.append(('ERROR', 'INDIVIDUAL', 'US10',
                                      (indi.repo['BIRT']['line'], fam.repo['MARR']['line']), indi.indi_id,
                                      error_message))
                if indi.indi_id == wife_id:
                    wife_birth = indi.repo['BIRT']['detail']
                    if abs((marriage_date - wife_birth).days / 365.25) < 14:
                        error_message = f'Wife:<{indi.indi_id}> marriage before she is 14 years old.'
                        error.append(('ERROR', 'INDIVIDUAL', 'US10',
                                      (indi.repo['BIRT']['line'], fam.repo['MARR']['line']), indi.indi_id,
                                      error_message))

        else:
            error_message = f'Family <{fam.fam_id}> do not have marriage date.'
            error.append(('ANOMALY', 'FAMILY', 'US10', fam.id_line, fam.fam_id, error_message))

    return error
