# -*- coding: utf-8 -*-
'''
    :codeauthor: :email:`Pedro Algarvio (pedro@algarvio.me)`
    :copyright: © 2015 by the SaltStack Team, see AUTHORS for more details.
    :license: Apache 2.0, see LICENSE for more details.


    pytestsalt.fixtures.dirs
    ~~~~~~~~~~~~~~~~~~~~~~~~

    pytest salt directories related fixtures
'''
# pylint: disable=redefined-outer-name

# Import Python libs
from __future__ import absolute_import
import logging

# Import 3rd-party libs
import pytest

pytest_plugins = ('tempdir', 'catchlog')  # pylint: disable=invalid-name

log = logging.getLogger(__name__)

ROOT_DIR = 'root'
CLI_ROOT_DIR = 'cli-root'
SESSION_ROOT_DIR = 'session-root'
SESSION_CLI_ROOT_DIR = 'session-cli-root'


@pytest.fixture
def root_dir(tempdir):
    '''
    Return the function scoped salt root dir
    '''
    dirname = tempdir.join(ROOT_DIR)
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def cli_root_dir(tempdir):
    '''
    Return the function scoped salt CLI root dir
    '''
    return tempdir.mkdir(CLI_ROOT_DIR)


@pytest.fixture(scope='session')
def session_root_dir(tempdir):
    '''
    Return the session scoped salt root dir
    '''
    return tempdir.mkdir(SESSION_ROOT_DIR)


@pytest.fixture(scope='session')
def session_cli_root_dir(tempdir):
    '''
    Return the session scoped salt CLI root dir
    '''
    return tempdir.mkdir(SESSION_CLI_ROOT_DIR)


@pytest.fixture
def conf_dir(root_dir):
    '''
    Fixture which returns the salt configuration directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = root_dir.join('conf')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def cli_conf_dir(cli_root_dir):
    '''
    Fixture which returns the salt configuration directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = cli_root_dir.join('conf')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def master_config_includes_dir(conf_dir):
    '''
    Fixture which returns the salt master configuration includes directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = conf_dir.join('master.d')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def minion_config_includes_dir(conf_dir):
    '''
    Fixture which returns the salt minion configuration includes directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = conf_dir.join('minion.d')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def cli_master_config_includes_dir(cli_conf_dir):
    '''
    Fixture which returns the salt master configuration includes directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = cli_conf_dir.join('master.d')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def cli_minion_config_includes_dir(cli_conf_dir):
    '''
    Fixture which returns the salt minion configuration includes directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = cli_conf_dir.join('minion.d')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def integration_files_dir(root_dir):
    '''
    Fixture which returns the salt integration files directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = root_dir.join('integration-files')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def cli_integration_files_dir(cli_root_dir):
    '''
    Fixture which returns the salt integration files directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = cli_root_dir.join('integration-files')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def state_tree_root_dir(integration_files_dir):
    '''
    Fixture which returns the salt state tree root directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = integration_files_dir.join('state-tree')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def pillar_tree_root_dir(integration_files_dir):
    '''
    Fixture which returns the salt pillar tree root directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = integration_files_dir.join('pillar-tree')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def base_env_state_tree_root_dir(state_tree_root_dir):
    '''
    Fixture which returns the salt base environment state tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = state_tree_root_dir.join('base')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def prod_env_state_tree_root_dir(state_tree_root_dir):
    '''
    Fixture which returns the salt prod environment state tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = state_tree_root_dir.join('prod')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def base_env_pillar_tree_root_dir(pillar_tree_root_dir):
    '''
    Fixture which returns the salt base environment pillar tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = pillar_tree_root_dir.join('base')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def prod_env_pillar_tree_root_dir(pillar_tree_root_dir):
    '''
    Fixture which returns the salt prod environment pillar tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = pillar_tree_root_dir.join('prod')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def cli_state_tree_root_dir(cli_integration_files_dir):
    '''
    Fixture which returns the salt state tree root directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = cli_integration_files_dir.join('state-tree')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def cli_pillar_tree_root_dir(cli_integration_files_dir):
    '''
    Fixture which returns the salt pillar tree root directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = cli_integration_files_dir.join('pillar-tree')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def cli_base_env_state_tree_root_dir(cli_state_tree_root_dir):
    '''
    Fixture which returns the salt base environment state tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = cli_state_tree_root_dir.join('base')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def cli_prod_env_state_tree_root_dir(cli_state_tree_root_dir):
    '''
    Fixture which returns the salt prod environment state tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = cli_state_tree_root_dir.join('prod')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def cli_base_env_pillar_tree_root_dir(cli_pillar_tree_root_dir):
    '''
    Fixture which returns the salt base environment pillar tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = cli_pillar_tree_root_dir.join('base')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture
def cli_prod_env_pillar_tree_root_dir(cli_pillar_tree_root_dir):
    '''
    Fixture which returns the salt prod environment pillar tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = cli_pillar_tree_root_dir.join('prod')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_conf_dir(session_root_dir):
    '''
    Fixture which returns the salt configuration directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_root_dir.join('conf')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_cli_conf_dir(session_cli_root_dir):
    '''
    Fixture which returns the salt configuration directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_cli_root_dir.join('conf')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_master_config_includes_dir(session_conf_dir):
    '''
    Fixture which returns the salt master configuration includes directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_conf_dir.join('master.d')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_minion_config_includes_dir(session_conf_dir):
    '''
    Fixture which returns the salt minion configuration includes directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_conf_dir.join('minion.d')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_cli_master_config_includes_dir(session_cli_conf_dir):
    '''
    Fixture which returns the salt master configuration includes directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_cli_conf_dir.join('master.d')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_cli_minion_config_includes_dir(session_cli_conf_dir):
    '''
    Fixture which returns the salt minion configuration includes directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_cli_conf_dir.join('minion.d')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_integration_files_dir(session_root_dir):
    '''
    Fixture which returns the salt integration files directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_root_dir.join('integration-files')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_cli_integration_files_dir(session_cli_root_dir):
    '''
    Fixture which returns the salt integration files directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_cli_root_dir.join('integration-files')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_state_tree_root_dir(session_integration_files_dir):
    '''
    Fixture which returns the salt state tree root directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_integration_files_dir.join('state-tree')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_pillar_tree_root_dir(session_integration_files_dir):
    '''
    Fixture which returns the salt pillar tree root directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_integration_files_dir.join('pillar-tree')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_base_env_state_tree_root_dir(session_state_tree_root_dir):
    '''
    Fixture which returns the salt base environment state tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_state_tree_root_dir.join('base')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_prod_env_state_tree_root_dir(session_state_tree_root_dir):
    '''
    Fixture which returns the salt prod environment state tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_state_tree_root_dir.join('prod')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_base_env_pillar_tree_root_dir(session_pillar_tree_root_dir):
    '''
    Fixture which returns the salt base environment pillar tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_pillar_tree_root_dir.join('base')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_prod_env_pillar_tree_root_dir(session_pillar_tree_root_dir):
    '''
    Fixture which returns the salt prod environment pillar tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_pillar_tree_root_dir.join('prod')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_cli_state_tree_root_dir(session_cli_integration_files_dir):
    '''
    Fixture which returns the salt state tree root directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_cli_integration_files_dir.join('state-tree')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_cli_pillar_tree_root_dir(session_cli_integration_files_dir):
    '''
    Fixture which returns the salt pillar tree root directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_cli_integration_files_dir.join('pillar-tree')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_cli_base_env_state_tree_root_dir(session_cli_state_tree_root_dir):
    '''
    Fixture which returns the salt base environment state tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_cli_state_tree_root_dir.join('base')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_cli_prod_env_state_tree_root_dir(session_cli_state_tree_root_dir):
    '''
    Fixture which returns the salt prod environment state tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_cli_state_tree_root_dir.join('prod')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_cli_base_env_pillar_tree_root_dir(session_cli_pillar_tree_root_dir):
    '''
    Fixture which returns the salt base environment pillar tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_cli_pillar_tree_root_dir.join('base')
    dirname.ensure(dir=True)
    return dirname


@pytest.fixture(scope='session')
def session_cli_prod_env_pillar_tree_root_dir(session_cli_pillar_tree_root_dir):
    '''
    Fixture which returns the salt prod environment pillar tree directory path.
    Creates the directory if it does not yet exist.
    '''
    dirname = session_cli_pillar_tree_root_dir.join('prod')
    dirname.ensure(dir=True)
    return dirname
