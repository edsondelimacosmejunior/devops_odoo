def buscar_modulo(models, db, uid, password, nome):
    modulo = models.execute_kw(db, uid, password,
                               'ir.module.module', 'search',
                               [[('name', 'like', nome)]])

    if modulo:
        return modulo[0]
    else:
        return False


def atualizar_modulo(models, db, uid, password, modulo):
    models.execute_kw(db, uid, password,
                      'ir.module.module', 'button_immediate_upgrade',
                      [modulo])