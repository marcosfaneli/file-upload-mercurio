import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AuthService } from './auth.service';

@Injectable()
export class EnsureAuthenticatedService implements CanActivate {

  constructor(private auth: AuthService, private router: Router) { }

  canActivate(): boolean {
    if (localStorage.getItem('token')) {
      return true;
    }

    this.router.navigateByUrl('/login');
    return false;
  }
}

