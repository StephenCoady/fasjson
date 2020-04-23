import ldap

from fasjson.web import errors, utils


def user(username):
    ldap_client = utils.ldap_client()

    try:
        res = ldap_client.get_user(username)
    except ldap.LOCAL_ERROR as e:
        raise errors.WebApiError(
            "LDAP local error", 500, data={"exception": str(e)}
        )

    if not res:
        raise errors.WebApiError(
            "user not found", 404, data={"username": username}
        )
    output = {"result": res}

    return output, 200
