import { TestBed } from '@angular/core/testing';

import { GameboxService } from './gamebox.service';

describe('GameboxService', () => {
  let service: GameboxService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GameboxService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
