def charger_image(nom):
    image = []
    L = []
    fmt, h, l, maxi = None, None, None, None
    with open(nom) as f:
        ligne = f.readline()

        while ligne:
            for c in ligne.split():
                commentaire = False
                if c[0] == '#': break
                elif "#" in c:
                    c = c[:c.index("#")]
                    commentaire = True
                if fmt is None: 
                    if c == 'P1':
                        fmt = 'PBM'
                        maxi = 0
                    elif c == 'P2': fmt = 'PGM'
                    elif c == 'P3': fmt = 'PPM'
                    elif c == 'X1':
                        fmt = 'PBMX'
                        maxi = 0
                    elif c == 'X2': fmt = 'PGMX'
                    elif c == 'X3': fmt = 'PPMX'
                    elif c == 'V1': fmt = 'PBMV'
                    elif c == 'V2': fmt = 'PGMV'
                    elif c == 'V3': fmt = 'PPMV'
                    else: raise ValueError("format {} non reconnu".format(fmt))
                elif l is None: l = int(c)
                elif h is None: h = int(c)
                elif maxi is None: maxi = int(c) 
                else: L.append(c)
                if commentaire: break

            ligne = f.readline()

    if fmt[-1] == 'V':
        if fmt[1] == 'P':
            fond = tuple(int(c) for c in L[:3])
            k = 3
        else:
            fond = int(L[0])
            k = 1
        objets = []
        while k < len(L):
            forme = L[k]
            coord = (int(L[k+1]), int(L[k+2]))
            if forme == 'rectangle':
                dim = (int(L[k+3]), int(L[k+4]))
                ind_c = k+5
            else:
                dim = (int(L[k+3]),)
                ind_c = k+4
            if fmt[1] == 'P':
                if len(dim) == 1:
                    objets.append((forme, coord[0], coord[1], dim[0], tuple(int(c) for c in L[ind_c:ind_c+3])))
                else:
                    objets.append((forme, coord[0], coord[1], dim[0], dim[1], tuple(int(c) for c in L[ind_c:ind_c+3])))
                k = ind_c + 3
            else:
                if len(dim) == 1:
                    objets.append((forme, coord[0], coord[1], dim[0], int(L[ind_c])))
                else:
                    objets.append((forme, coord[0], coord[1], dim[0], dim[1], int(L[ind_c])))
                k = ind_c + 1
        return (l, h, fond, objets), fmt, maxi

    
    L = [int(c) for c in L]

    if fmt[-1] == 'X':
        k = 0
        ligne = []
        cpt = 0
        while k < len(L):
            if fmt[1] in ['B', 'G']:
                ligne.append((L[k], L[k+1]))
                cpt += L[k]
                k += 2
            else:
                ligne.append((L[k],(L[k+1],L[k+2],L[k+3])))
                cpt += L[k]
                k += 4
            if cpt == l:
                image.append(ligne)
                ligne = []
                cpt = 0

    elif fmt[1] in ['B', 'G']:
        for i in range(h):
            image.append(L[i*l:(i+1)*l])
    else:
        for i in range(h):
            image.append([tuple(L[3*j:3*j+3]) for j in range(i*l,(i+1)*l)])

    return image, fmt, maxi


def sauver_image(image, fmt, nom, maxi = 0):
    if fmt == 'PBM':
        l1, ext = 'P1', '.pbm'
    elif fmt == 'PGM':
        l1, ext = 'P2', '.pgm'
    elif fmt == 'PPM':
        l1, ext = 'P3', '.ppm'
    elif fmt == 'PBMX':
        l1, ext = 'X1', '.pbmx'
    elif fmt == 'PGMX':
        l1, ext = 'X2', '.pgmx'
    elif fmt == 'PPMX':
        l1, ext = 'X3', '.ppmx'
    elif fmt == 'PBMV':
        l1, ext = 'V1', '.pbmv'
    elif fmt == 'PGMV':
        l1, ext = 'V2', '.pgmv'
    elif fmt == 'PPMV':
        l1, ext = 'V3', '.ppmv'
    else: raise ValueError('fmt {} non reconnu'.format(fmt))

    if maxi == 0:
        if fmt == 'PGM': maxi = max(max(ligne) for ligne in image) 
        elif fmt == 'PPM': maxi = max(max(max(t) for t in ligne) for ligne in image)
        elif fmt == 'PGMX': maxi = max(max(t[1] for t in ligne) for ligne in image)
        elif fmt == 'PPMX': maxi = max(max(max(t[1]) for t in ligne) for ligne in image)
        elif fmt == 'PGMV': maxi = max(t[-1] for t in image[-1])
        elif fmt == 'PPMV': maxi = max(max(t[-1]) for t in image[-1])

    with open(nom+ext, 'w') as f:
        f.write(l1+'\n')
        if fmt[-1] == 'X':
            l = 0
            for ll, _ in image[0]:
                l += ll
            f.write('{} {}\n'.format(l, len(image)))
        elif fmt[-1] == 'V':
            f.write('{} {}\n'.format(image[0], image[1]))
        else:
            f.write('{} {}\n'.format(len(image[0]), len(image)))

        if fmt[1] in ['G', 'P']: 
            f.write('{}\n'.format(maxi))

        if fmt[-1] == 'V':
            f.write('{}\n'.format(image[2]) if fmt[1] != 'P' else '{} {} {}\n'.format(*image[2]))
            for ob in image[3]:
                f.write('{} {} {} {} '.format(*ob))
                ind_c = 4
                if ob[0] == 'rectangle':
                    f.write('{} '.format(ob[4]))
                    ind_c = 5
                f.write('{}\n'.format(ob[ind_c]) if fmt[1] != 'P' else '{} {} {}\n'.format(*ob[ind_c]))

            return

        for ligne in image:
            n = 0
            for c in ligne:
                couleur = ''
                if fmt[-1] == 'X': # Formats compressés
                    couleur = '{} '.format(c[0])
                    c = c[1]
                couleur += '{}'.format(c) if fmt[1] != 'P' else '{} {} {}'.format(*c)
                if n == 0:
                    f.write(couleur)
                    n += len(couleur)
                elif n + len(couleur) < 70:
                    f.write(' ' + couleur)
                    n += 1 + len(couleur)
                else:
                    f.write('\n' + couleur)
                    n = len(couleur)
            f.write('\n')

