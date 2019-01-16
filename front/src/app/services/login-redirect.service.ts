import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AuthService } from './auth.service';

@Injectable()
export class LoginRedirectService implements CanActivate {

  constructor(private auth: AuthService, private router: Router) { }

  canActivate(): boolean {
      if (localStorage.getItem('token')) {
        this.router.navigateByUrl('logout');
        return false;
      }

      return true;
    }
}
